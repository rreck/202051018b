```json
{
  "id": "6341f98481b81b3d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287907,
  "host_pid": "9e6742732c60:1",
  "hash": "af081a6bedfbb87ada6700e568f93cc7de3c84eb576132c0fd5f99e2ade2e7e0",
  "cid": "QmV1af081a6bedfbb87ada6700e568f93cc7de3c84eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287907,
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
      "evaluated_at": 1760287907
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
  "sig": "da140f8c2c6d7b80cb6a183e506fed951bcaa5deae660a0ab238dd6a702a88b1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598542542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 25418276, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285764, 'matching_hash': '3cc1c7bbce52acf6'}}}