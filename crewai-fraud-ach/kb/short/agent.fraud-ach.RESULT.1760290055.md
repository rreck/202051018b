```json
{
  "id": "e35be223adce3fe1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290055,
  "host_pid": "9e6742732c60:1",
  "hash": "395f29f001552d5b7121afb70c41350a213cdbc38e536be4faab0b908a2126c6",
  "cid": "QmV1395f29f001552d5b7121afb70c41350a213cdbc3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290055,
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
      "evaluated_at": 1760290055
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
  "sig": "f679f2e3342090d89034d4fdb095d2cc7335c4cea249979d694e21cbbdf586d4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279280277
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 61841500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285763, 'matching_hash': '5e64cdd29eaed333'}}}