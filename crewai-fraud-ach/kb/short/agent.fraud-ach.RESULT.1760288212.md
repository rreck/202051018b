```json
{
  "id": "919549c50768cc40",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288212,
  "host_pid": "9e6742732c60:1",
  "hash": "5ad1b7e2c842025702909f8bc938096f108498e3ecef811800dd75b30278ad83",
  "cid": "QmV15ad1b7e2c842025702909f8bc938096f108498e3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288212,
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
      "evaluated_at": 1760288212
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
  "sig": "78e70b40a0635167fc680be975d8645fd94578661880c14d0450bcb6d6e3c8b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154440687
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 24098146, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285763, 'matching_hash': '04c13f034fff9f4d'}}}