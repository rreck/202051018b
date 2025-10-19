```json
{
  "id": "9aa26063b707c2cb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293726,
  "host_pid": "9e6742732c60:1",
  "hash": "443c1e7576d9f2c1ec56d1057cf732863e4873aea48e0e30b5b7a0d9c067caaa",
  "cid": "QmV1443c1e7576d9f2c1ec56d1057cf732863e4873ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293726,
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
      "evaluated_at": 1760293726
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
  "sig": "656bdcb5217d9c2b7fbda836b35a4c17d85e3ea818887774dcbe89e5b070fcd1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598500621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 79881984, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': '36e427bddf577026'}}}