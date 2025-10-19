```json
{
  "id": "d7aaf1b9a9f88278",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291705,
  "host_pid": "9e6742732c60:1",
  "hash": "00c03e5c2eccb31edcbe579386da28435b4605a96d23206a4fd64bc851552e9c",
  "cid": "QmV100c03e5c2eccb31edcbe579386da28435b4605a9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291705,
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
      "evaluated_at": 1760291705
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
  "sig": "efee47fd9a8c738743a43a6eb027353404894cb687e769e101219d1c56593302"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030595065
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 55000651, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': '3889a0f66c8870f8'}}}