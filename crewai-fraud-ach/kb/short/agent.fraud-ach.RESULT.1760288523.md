```json
{
  "id": "420c5e38d14aef0f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288523,
  "host_pid": "9e6742732c60:1",
  "hash": "196b0928cf05a22b6fdcf789592698072edb850ae46b57e1215203ab373c3c8d",
  "cid": "QmV1196b0928cf05a22b6fdcf789592698072edb850a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288523,
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
      "evaluated_at": 1760288523
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
  "sig": "42fb599b7cdc2916790d406d8013005cfd5cbb72b5673bd735a777f44965370b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028116675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 32677920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285763, 'matching_hash': '276303153292771e'}}}