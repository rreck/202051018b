```json
{
  "id": "1fc0ebb033d490cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293651,
  "host_pid": "9e6742732c60:1",
  "hash": "4b601bf18cb3b3ad790b76f95f86233abaade30042db5c58940b91ea1ef7cb57",
  "cid": "QmV14b601bf18cb3b3ad790b76f95f86233abaade300",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293651,
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
      "evaluated_at": 1760293651
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
  "sig": "2386a05385844b138349f90469b802f7e3b4fe75ba72e2a916e3e5c03cbc1303"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462098783
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 45860842, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': '4ea38d6416e4381e'}}}