```json
{
  "id": "4f0401c29b4e6ee8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291277,
  "host_pid": "9e6742732c60:1",
  "hash": "05cb492bd4ed88c783ad0575f939868dfe3b5cfbd8e8e71cfeb1abdb80335410",
  "cid": "QmV105cb492bd4ed88c783ad0575f939868dfe3b5cfb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291277,
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
      "evaluated_at": 1760291277
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
  "sig": "9e5314397a8236918402b16cea6d55503813ceaa06417aedd76fc378c4d35d78"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595571766
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 84060009, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': '7b9b43f48a0de4d3'}}}