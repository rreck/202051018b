```json
{
  "id": "1b753a215e097ecd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288342,
  "host_pid": "9e6742732c60:1",
  "hash": "6d124f426e831445ba22139e29dc523c3d567f5092fe19128789cb96393039f0",
  "cid": "QmV16d124f426e831445ba22139e29dc523c3d567f50",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288342,
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
      "evaluated_at": 1760288342
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
  "sig": "64862954f6b1f61a8c41e92ddf0573a45e145cd25f9c20eea2d2b58c89a0ef39"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 011137004104696
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 90, 'threshold': 50, 'total_amount': 10983510, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 89, 'first_seen': 1760285765, 'matching_hash': 'b4a76c6b789f42f2'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '011137004', 'validation_error': 'Invalid routing number checksum'}}}