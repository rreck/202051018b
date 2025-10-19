```json
{
  "id": "ac12d7476ecda392",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289877,
  "host_pid": "9e6742732c60:1",
  "hash": "e16d1c428ec4765d0e387a8fdd1c14c59aace1586f45d9cbb981455fc77a261d",
  "cid": "QmV1e16d1c428ec4765d0e387a8fdd1c14c59aace158",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289877,
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
      "evaluated_at": 1760289877
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
  "sig": "d75c13874e4046fec37186ad44261cbe4d4815dc9ee32cade18f3250cbf4599b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274571178
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 64254195, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285765, 'matching_hash': '2fe0a786c074c752'}}}