```json
{
  "id": "bbfdd8c1ac8deb72",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294326,
  "host_pid": "9e6742732c60:1",
  "hash": "8f91903613b19bd6474c00fe78c462c7d8f0f70c61ff863d7d5778be718aeab3",
  "cid": "QmV18f91903613b19bd6474c00fe78c462c7d8f0f70c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294326,
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
      "evaluated_at": 1760294326
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
  "sig": "f1b61c3a8e267e7dbb3527c962a7b3b0f41137a8cd1129eeb42084b0c7dc4ec9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247065619
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 94368612, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': '73a93f9011d99735'}}}