```json
{
  "id": "738e6d87281fd9ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294373,
  "host_pid": "9e6742732c60:1",
  "hash": "50a4175aa168c23a48457f6540c2b871437847a71f787b127d207fa5ec30a5d5",
  "cid": "QmV150a4175aa168c23a48457f6540c2b871437847a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294373,
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
      "evaluated_at": 1760294374
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
  "sig": "dd0ba767eb3ffccf293dade6d1232c808c51a50b14769bfae2fe345b82b77569"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029996971
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 24651081, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': '92fd98aa1089d1f1'}}}