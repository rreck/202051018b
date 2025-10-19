```json
{
  "id": "74b8cfe0db93c48b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294119,
  "host_pid": "9e6742732c60:1",
  "hash": "a7d8072b63435714aa350abe721a2dbc0368aa2349418e56035c2f44ecbdad44",
  "cid": "QmV1a7d8072b63435714aa350abe721a2dbc0368aa23",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294119,
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
      "evaluated_at": 1760294119
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
  "sig": "9d82d3f5e61642310f01464b8991bf29b61022431593a40bb1bfaea0d3eeaeee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024298856
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 79179280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': 'c651031c314af1fc'}}}