```json
{
  "id": "86eac5ea3502be92",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291969,
  "host_pid": "9e6742732c60:1",
  "hash": "17bd97fa25140d3cd38663349742bcd9dcebca84163d06e336d6388de459945e",
  "cid": "QmV117bd97fa25140d3cd38663349742bcd9dcebca84",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291969,
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
      "evaluated_at": 1760291969
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
  "sig": "dd06f512b5006e230063382bb348a939744b2ec097facbfcea86556904b6f6f9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466272908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 69999897, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285765, 'matching_hash': 'c5e3c9a8e5c19188'}}}