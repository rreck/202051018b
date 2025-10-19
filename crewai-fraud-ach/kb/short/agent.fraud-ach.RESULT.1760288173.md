```json
{
  "id": "4b6b0873779c6937",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288173,
  "host_pid": "9e6742732c60:1",
  "hash": "e8756bdf264e833b192122b81138ecbd5a623d018805cd2a278ac97cc524cbb3",
  "cid": "QmV1e8756bdf264e833b192122b81138ecbd5a623d01",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288173,
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
      "evaluated_at": 1760288173
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
  "sig": "b4989d1daac092b24539051ceecc1b8672a8a0f10067e029269343d7f46d6c10"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249232395
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 31028060, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285764, 'matching_hash': '83f71011b8a0f970'}}}