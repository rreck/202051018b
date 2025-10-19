```json
{
  "id": "26de8c579387a89f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293262,
  "host_pid": "9e6742732c60:1",
  "hash": "a25097fd4a607794d8fda94c8dd79df9c2afdec8ef8c1c8c7327e525db5da831",
  "cid": "QmV1a25097fd4a607794d8fda94c8dd79df9c2afdec8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293262,
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
      "evaluated_at": 1760293262
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "613c397ea5e64782fd3f9e5cf57b49bbceea2e0ebf926f61be844561def56c58"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027419247
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 101011515, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': 'f49fdb64c00c5aec'}}}