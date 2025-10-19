```json
{
  "id": "72005293ab1a87fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293245,
  "host_pid": "9e6742732c60:1",
  "hash": "6a62cbca9b2dbf4961f16c8293b0f8c3d7e11f97c6f0b76be0d4742d3429d9ea",
  "cid": "QmV16a62cbca9b2dbf4961f16c8293b0f8c3d7e11f97",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293245,
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
      "evaluated_at": 1760293245
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
  "sig": "b9ba2d48de86f99cb5b9b0e08992e8c5a45c116c725fc674131a7e20755a3946"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025339678
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 86373396, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285765, 'matching_hash': '57e7473926bfe00b'}}}