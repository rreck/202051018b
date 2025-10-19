```json
{
  "id": "2f08467d1dbac978",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290995,
  "host_pid": "9e6742732c60:1",
  "hash": "79f208f5ddccec9522af216d31e65972524c6bf9de157691b83b9b1737d2cbbc",
  "cid": "QmV179f208f5ddccec9522af216d31e65972524c6bf9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290995,
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
      "evaluated_at": 1760290995
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
  "sig": "cbec3a120ad07052d2d24c985f9f97ea21f04ad3546bb7c6a1e0878c76ed1c9a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152430853
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 13823068, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285764, 'matching_hash': 'fa17beca2cfad33c'}}}