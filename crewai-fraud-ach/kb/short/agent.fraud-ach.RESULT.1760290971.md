```json
{
  "id": "cee319212d07d0f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290971,
  "host_pid": "9e6742732c60:1",
  "hash": "fe074ca7ff71343c2d36e3f77210ddd95afa7443f74cf6beaa9a9daccf9cf8ac",
  "cid": "QmV1fe074ca7ff71343c2d36e3f77210ddd95afa7443",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290971,
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
      "evaluated_at": 1760290971
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
  "sig": "ac93d6c67c3df4244fe4dfeb8fdf63cfce9cde1e072545b2ac617be80249ab2d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037990803
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 38171000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': 'be616144f18eac0b'}}}