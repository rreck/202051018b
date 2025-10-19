```json
{
  "id": "0d48103e9f6d7f49",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293247,
  "host_pid": "9e6742732c60:1",
  "hash": "d34d2959ab404fb1f6528f02ff7e3cc526308c5b17ac9fb9bcd6a9ced7339194",
  "cid": "QmV1d34d2959ab404fb1f6528f02ff7e3cc526308c5b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293247,
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
      "evaluated_at": 1760293247
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
  "sig": "68c49f400f9104ba856b53418224c5408f37836ab6e09fd768b64dc515f0ce98"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 68105072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}