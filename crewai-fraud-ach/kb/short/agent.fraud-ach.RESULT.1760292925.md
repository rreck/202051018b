```json
{
  "id": "12565c5652f07f89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292925,
  "host_pid": "9e6742732c60:1",
  "hash": "5a60c2cf9ad0797d2659bb5b2e8f7958aecabc68c4c4cc18d20ef19af5cded4f",
  "cid": "QmV15a60c2cf9ad0797d2659bb5b2e8f7958aecabc68",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292925,
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
      "evaluated_at": 1760292926
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
  "sig": "21a949ae52956ee1cb3e8490661554d0ccf8cefa4f3b4a2bb73dbb780ca27ae7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241647784
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 22866272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285763, 'matching_hash': '5747783cddc76b25'}}}