```json
{
  "id": "0f637de7776d2d5e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290813,
  "host_pid": "9e6742732c60:1",
  "hash": "3ecab6c946b986b389ffcd1875dee0a12b3662721b9286e90039dcebb2610193",
  "cid": "QmV13ecab6c946b986b389ffcd1875dee0a12b366272",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290813,
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
      "evaluated_at": 1760290813
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
  "sig": "a7e111e28925e59b6bd27fed40279035cd57f007163c675a6039c902f7bbfc60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028270724
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 160, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 159, 'first_seen': 1760285763, 'matching_hash': 'c4ee7f0f971d402b'}}}een': 1760285763, 'matching_hash': '73a93f9011d99735'}}}