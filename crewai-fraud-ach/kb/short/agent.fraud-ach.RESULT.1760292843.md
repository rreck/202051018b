```json
{
  "id": "8c602bc6ddf08650",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292843,
  "host_pid": "9e6742732c60:1",
  "hash": "2a642d456eba6dd99af19a6afd69712a6d3284879b822242597ab3c30c7da575",
  "cid": "QmV12a642d456eba6dd99af19a6afd69712a6d328487",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292843,
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
      "evaluated_at": 1760292843
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
  "sig": "a25b20e03a8bfa512b68cd3b432779bc1fe29aefbc167fa2eb50544a29056eac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029664164
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 96737394, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285764, 'matching_hash': '915cdda6adcb6880'}}}