```json
{
  "id": "03d0db3bbc548362",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294330,
  "host_pid": "9e6742732c60:1",
  "hash": "f10946f8f886153836010f58b4cd30d8c93876b92b402617a9937f922a1778db",
  "cid": "QmV1f10946f8f886153836010f58b4cd30d8c93876b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294330,
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
      "evaluated_at": 1760294330
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
  "sig": "7e90fcf3e93bbf741cb213be537d8a556ca1b268daeb32d66e17d59a05ead940"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241330040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 62910520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '556aef048193b362'}}}