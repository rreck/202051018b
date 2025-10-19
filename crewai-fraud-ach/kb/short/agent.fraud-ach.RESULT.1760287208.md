```json
{
  "id": "163fcec1be70600e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287208,
  "host_pid": "9e6742732c60:1",
  "hash": "84adc80847bf0aa51dbe149bf95f184a6501aef28977730be14b890120864395",
  "cid": "QmV184adc80847bf0aa51dbe149bf95f184a6501aef2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287208,
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
      "evaluated_at": 1760287208
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "69461411cab09bc0df9d794eb76656775299504778bafbdb25798740db075497"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009598152937
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 13000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285763, 'matching_hash': '12ca21f72ace6b8c'}}}