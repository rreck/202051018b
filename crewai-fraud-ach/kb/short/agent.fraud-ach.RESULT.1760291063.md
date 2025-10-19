```json
{
  "id": "a922033586ec0aba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291063,
  "host_pid": "9e6742732c60:1",
  "hash": "df406aac725ab692cb941a98b6712d9ba31514b25ad092335074176137857f83",
  "cid": "QmV1df406aac725ab692cb941a98b6712d9ba31514b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291063,
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
      "evaluated_at": 1760291063
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
  "sig": "ab4f86e06226ded124326ce5f73845fcff7a0fcb62aa91d739aed6f155dc5637"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271137444
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 166, 'threshold': 50, 'total_amount': 37616596, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 165, 'first_seen': 1760285763, 'matching_hash': 'cc450f1d426424de'}}}