```json
{
  "id": "d538a52450267efa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293186,
  "host_pid": "9e6742732c60:1",
  "hash": "10fcb69801701d79f8905773e17f8cc6d501c5751179cd187287588f5d210ba4",
  "cid": "QmV110fcb69801701d79f8905773e17f8cc6d501c575",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293186,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760293186
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "ed7803d55f856873dcf64f3563e5b388ee81aff5af5c137ab3e7c1bc7e7ef5a6"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 789209528183836
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 55539111, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285765, 'matching_hash': 'e8f44f77b3005867'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '789209527', 'validation_error': 'Invalid routing number checksum'}}}