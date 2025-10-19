```json
{
  "id": "c0a0edeb4a5ffc09",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289604,
  "host_pid": "9e6742732c60:1",
  "hash": "79a5c5d64c27f5480ed0146ded309ece30e9cf474efd93b5dedcf917274fb262",
  "cid": "QmV179a5c5d64c27f5480ed0146ded309ece30e9cf47",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289604,
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
      "evaluated_at": 1760289604
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
  "sig": "a61afc1fdc0ea62223c52709e2276d8442d606cbe71aabbf5d9d5fd2c18237b5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598219972
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 62587264, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285763, 'matching_hash': '09b5d296b49f9602'}}}