```json
{
  "id": "a99d92df1203f95a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290736,
  "host_pid": "9e6742732c60:1",
  "hash": "e9de31fcd49a494fc6e42cf283158c4720380f7862b7d1488e0f90692a236d82",
  "cid": "QmV1e9de31fcd49a494fc6e42cf283158c4720380f78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290736,
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
      "evaluated_at": 1760290736
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
  "sig": "e860bf4325adb471bb229a7bb8efe35cbddf248641458e2f1d394072b73cb02d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026865262
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 77379078, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285763, 'matching_hash': 'acc989ae5f5d7052'}}}