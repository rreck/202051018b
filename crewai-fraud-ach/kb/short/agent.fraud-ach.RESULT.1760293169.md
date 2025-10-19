```json
{
  "id": "6fe5e84237992ecf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293169,
  "host_pid": "9e6742732c60:1",
  "hash": "c09f8fa61b08ad3ecaf28c8e57787904c5e2f63b0eb1bf58467e8f74b68483d7",
  "cid": "QmV1c09f8fa61b08ad3ecaf28c8e57787904c5e2f63b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293169,
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
      "evaluated_at": 1760293169
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
  "sig": "4c937594cbaae3be52d0a9a800554535c9244293c5a3db4fb6a1c3ae6c78cb27"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241053391
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 91266879, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '6e04470f15e4fc18'}}}