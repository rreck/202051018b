```json
{
  "id": "df1b04afcf1c66e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294397,
  "host_pid": "9e6742732c60:1",
  "hash": "8e5fe6e50f5a3f83b42a38a658618c45080699dd00adb496ffc2a2ebac74ec3f",
  "cid": "QmV18e5fe6e50f5a3f83b42a38a658618c45080699dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294397,
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
      "evaluated_at": 1760294397
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
  "sig": "8165f7b2a9018fd45b0469749e40333774707f2e2fbfff93d6f0ac0b21191c63"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026281875
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 97103166, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': 'ee0b29e0b2882e41'}}}