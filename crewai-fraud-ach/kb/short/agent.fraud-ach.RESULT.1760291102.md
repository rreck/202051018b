```json
{
  "id": "4987652c1b9948d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291102,
  "host_pid": "9e6742732c60:1",
  "hash": "fa4a10785875351b8bd4b1ee713c2fd87290df54878bf0189f418eaf8bdc294c",
  "cid": "QmV1fa4a10785875351b8bd4b1ee713c2fd87290df54",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291102,
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
      "evaluated_at": 1760291102
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
  "sig": "8281c0dc510e3a540f8549795d79dcd7fac98aeb4875f6829264ccd5c29015cd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037688830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 42673844, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285764, 'matching_hash': 'a1e0090e71bf48f4'}}}