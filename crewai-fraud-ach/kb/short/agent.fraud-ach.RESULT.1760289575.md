```json
{
  "id": "215526aeffef6b48",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289575,
  "host_pid": "9e6742732c60:1",
  "hash": "81ac8975d3c0b1bd288b42b8cf18acca7accf4260cd1d7ebfa6f8c3ecd06f520",
  "cid": "QmV181ac8975d3c0b1bd288b42b8cf18acca7accf426",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289575,
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
      "evaluated_at": 1760289575
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
  "sig": "f1a5b701f4e463ea9d21220e3eccb8d01617a2bbe6b654929679456e1adc33d1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270162443
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 63123064, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285763, 'matching_hash': 'e637274c2d5e4084'}}}