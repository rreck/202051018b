```json
{
  "id": "13eb066ed7d0e0f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289300,
  "host_pid": "9e6742732c60:1",
  "hash": "1756081f9cfcaa4f359d24902597ee9acb36c89eb279a0550ea169f656b14680",
  "cid": "QmV11756081f9cfcaa4f359d24902597ee9acb36c89e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289300,
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
      "evaluated_at": 1760289300
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
  "sig": "b1c337d8113378d25b3b3928604a507f42d5dbc4a86b7436928be2b593eabe3e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027276119
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 33186720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285763, 'matching_hash': 'ec114b5b29b7d5ae'}}}