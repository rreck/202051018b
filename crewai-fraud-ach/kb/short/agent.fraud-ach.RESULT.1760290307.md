```json
{
  "id": "a994ad98fb0577a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290307,
  "host_pid": "9e6742732c60:1",
  "hash": "de82be9063d24a57da1a3b8573c950b08368ad2b6cfd0bfdef3067281ecef900",
  "cid": "QmV1de82be9063d24a57da1a3b8573c950b08368ad2b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290307,
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
      "evaluated_at": 1760290307
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
  "sig": "186e53a3f949b678623671db59992dd8e602be260454cecf8312aff256faa0ed"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026691588
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 147, 'threshold': 50, 'total_amount': 59486049, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 146, 'first_seen': 1760285763, 'matching_hash': '1da0382cf03ec7d2'}}}