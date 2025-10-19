```json
{
  "id": "86f5ef7a6a4b72e7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285946,
  "host_pid": "9e6742732c60:1",
  "hash": "0477643d8126820db250995ed41dda843db7fe65fab60da7706af50a7ece6d8f",
  "cid": "QmV10477643d8126820db250995ed41dda843db7fe65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285946,
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
      "evaluated_at": 1760285946
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
  "sig": "4bdae2dc14d347a1a3ee68bbcfe939d00e6d5781db93cd3b333fa017c5efbaba"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000037779899
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285765, 'matching_hash': '90378a324202fffb'}}}: 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760284979, 'matching_hash': '5ec025bcbfaa0fd9'}}}