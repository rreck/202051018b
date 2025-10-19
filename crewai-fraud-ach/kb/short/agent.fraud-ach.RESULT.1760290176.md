```json
{
  "id": "919d62bee6383def",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290176,
  "host_pid": "9e6742732c60:1",
  "hash": "139b10395ed99e26ca145a79139d91acacbbc3041814c3626530e2c9169e55db",
  "cid": "QmV1139b10395ed99e26ca145a79139d91acacbbc304",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290176,
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
      "evaluated_at": 1760290176
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
  "sig": "91a31e17626dce7d823f8194018c4cc79d8de69443ab7e8a54c79e690acdc067"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033965137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 20403240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285765, 'matching_hash': 'a94abbf708458614'}}}