```json
{
  "id": "e40159ca6f9b8693",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291540,
  "host_pid": "9e6742732c60:1",
  "hash": "eca5114eefbba1599c4bd284d38aea62689cccced28281106d98582d2d229a4b",
  "cid": "QmV1eca5114eefbba1599c4bd284d38aea62689cccce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291540,
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
      "evaluated_at": 1760291540
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
  "sig": "f043c2591b55afaead02b113f3612d887e3328b6904d24963a32237b19d590f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028366239
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 177, 'threshold': 50, 'total_amount': 24093594, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 176, 'first_seen': 1760285763, 'matching_hash': 'fc3cc28fddce4cc6'}}}