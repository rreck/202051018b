```json
{
  "id": "01e954a8865310f5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288444,
  "host_pid": "9e6742732c60:1",
  "hash": "9db4c1b6abd916ecc0c3fe11eed796c74d6e8069fd68f36b0fdf2b4e0ab69e5e",
  "cid": "QmV19db4c1b6abd916ecc0c3fe11eed796c74d6e8069",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288444,
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
      "evaluated_at": 1760288444
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
  "sig": "e2c4d5514686ecedc8f1722af26cf17f1c17d458269a61f29bb62f465344406e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 29597064, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}