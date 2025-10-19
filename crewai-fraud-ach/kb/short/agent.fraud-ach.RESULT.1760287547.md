```json
{
  "id": "cb0f30631c2f424e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287547,
  "host_pid": "9e6742732c60:1",
  "hash": "4958a028104d42b02e240d4dcdfeeacadb72d8c0f5aef5fd9bbb6dca2057120d",
  "cid": "QmV14958a028104d42b02e240d4dcdfeeacadb72d8c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287547,
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
      "evaluated_at": 1760287547
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
  "sig": "f17a339b72a905e1728b73535136ff732d6a25444bc66c32ba06f0f83964de7a"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 121000240979962
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 22759744, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285763, 'matching_hash': '0560549e1456bff1'}}}: {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6602570}}}