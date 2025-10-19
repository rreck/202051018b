```json
{
  "id": "44640632aeda7529",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288127,
  "host_pid": "9e6742732c60:1",
  "hash": "fd05abb58d5897152c90a49b5cd2b4c73eb217283ef1adc4643ef500a95061c0",
  "cid": "QmV1fd05abb58d5897152c90a49b5cd2b4c73eb21728",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288127,
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
      "evaluated_at": 1760288127
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
  "sig": "d16210782b59289c22f45569e46c2e2b13092071c9b5e12c9da1d4709b6448aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592654855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 25061269, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285765, 'matching_hash': '0ed93ea6dd0046b6'}}}