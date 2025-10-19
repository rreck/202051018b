```json
{
  "id": "927de5e48d4d29c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288998,
  "host_pid": "9e6742732c60:1",
  "hash": "2bb3dc9f19c8862803bab90751719d63e3cffdcf4eeae2684a365f5a655ad77b",
  "cid": "QmV12bb3dc9f19c8862803bab90751719d63e3cffdcf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288998,
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
      "evaluated_at": 1760288998
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
  "sig": "a856a24c7697b2472fbef78e79b06b18af909525fee8ce93a8e2366943bed5be"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025503816
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 43142000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285765, 'matching_hash': 'fc6cd7074b4844e3'}}}