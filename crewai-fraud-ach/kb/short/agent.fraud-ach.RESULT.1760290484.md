```json
{
  "id": "e65480138c973b16",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290484,
  "host_pid": "9e6742732c60:1",
  "hash": "bf33a5fe2db6ad75cd750f57ff7a923fe78037e8aae2f1737ab0f8403942e1ae",
  "cid": "QmV1bf33a5fe2db6ad75cd750f57ff7a923fe78037e8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290484,
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
      "evaluated_at": 1760290484
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
  "sig": "db89257e5b5514232f1abe67a01021e65038edfc80060ff63927fdee660be719"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 48055448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}