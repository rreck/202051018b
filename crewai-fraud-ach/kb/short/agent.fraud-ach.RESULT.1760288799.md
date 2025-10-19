```json
{
  "id": "ff5ffd3d0090c15a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288799,
  "host_pid": "9e6742732c60:1",
  "hash": "04cbfe75099cda64bffc897be27990f11877e344a4edff58af9a6b705075ee0e",
  "cid": "QmV104cbfe75099cda64bffc897be27990f11877e344",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288799,
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
      "evaluated_at": 1760288799
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
  "sig": "30c6200d6bd46df841599ca21498dafcf159072f84157b9aa8365d6302ebec8a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460625527
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 49937680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285765, 'matching_hash': 'd2e448c8360c8b26'}}}