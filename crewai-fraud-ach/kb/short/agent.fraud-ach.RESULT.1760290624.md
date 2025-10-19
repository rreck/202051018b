```json
{
  "id": "494994e97542a564",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290624,
  "host_pid": "9e6742732c60:1",
  "hash": "2ebe0bc1f9af163d1285d8fc6f17a42cd337ba44840269d8535ea3803b524b13",
  "cid": "QmV12ebe0bc1f9af163d1285d8fc6f17a42cd337ba44",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290624,
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
      "evaluated_at": 1760290624
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
  "sig": "48f2c62452c1c91fdc2bdf2888f199d5c167889f2f495754419accf5c70627a3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029384681
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 155, 'threshold': 50, 'total_amount': 14283250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 154, 'first_seen': 1760285764, 'matching_hash': '45a3ccbce684d395'}}}