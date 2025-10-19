```json
{
  "id": "7b70a3f297c62e82",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288066,
  "host_pid": "9e6742732c60:1",
  "hash": "5ab13f98b509780f4251a4430a60607f81976ce746970c2f9d02072732e97c42",
  "cid": "QmV15ab13f98b509780f4251a4430a60607f81976ce7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288066,
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
      "evaluated_at": 1760288066
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
  "sig": "358ee4e73b26ce91abbfcc8b852b667c8fe5e39147a64132563390ea85b398aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 25778088, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}