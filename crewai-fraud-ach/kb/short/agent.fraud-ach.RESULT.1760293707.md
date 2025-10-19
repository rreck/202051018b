```json
{
  "id": "93cdc64fccea7fc9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293707,
  "host_pid": "9e6742732c60:1",
  "hash": "83dccfce1ff0a75706d3256065cee5131727a3367a5c53ca3e6279f8030ad763",
  "cid": "QmV183dccfce1ff0a75706d3256065cee5131727a336",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293707,
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
      "evaluated_at": 1760293707
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
  "sig": "b06e8cb7ae18206c3f834cc9977aa743f2453907f842496c2537c062989fed43"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028841300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 41873440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': 'f5bed59f6c250fae'}}}