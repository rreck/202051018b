```json
{
  "id": "c537d19801de64fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290664,
  "host_pid": "9e6742732c60:1",
  "hash": "6207b2096a97d77e292f579f886600f8a24f88f9ee7692f95f033cee9f729202",
  "cid": "QmV16207b2096a97d77e292f579f886600f8a24f88f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290664,
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
      "evaluated_at": 1760290664
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
  "sig": "997e22dca3107ccbfc86ca56cb10d97d74d2c12b647374401eccfb0fd76dd514"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028413829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 24134448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': '35164be796d7e820'}}}