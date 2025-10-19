```json
{
  "id": "7630519f3c11ef9d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293554,
  "host_pid": "9e6742732c60:1",
  "hash": "bbf484777c64c5ff7ee7cf9a70fcbf912c2734a87b1cd761edd7963d5f8d693b",
  "cid": "QmV1bbf484777c64c5ff7ee7cf9a70fcbf912c2734a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293554,
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
      "evaluated_at": 1760293554
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
  "sig": "2ca54719c678b0361ce1c20094ee7ba72a14611c65a3be296523a9c9e7a07154"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590857246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 78323726, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': 'f091f96bdb04a5bf'}}}