```json
{
  "id": "fe8a9f0a24cbf176",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287467,
  "host_pid": "9e6742732c60:1",
  "hash": "61c2b858651db0503ddd22bad71ce207f78c9a61e8f5665db37328314c4350b9",
  "cid": "QmV161c2b858651db0503ddd22bad71ce207f78c9a61",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287467,
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
      "evaluated_at": 1760287467
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
  "sig": "ceb39f5586018cb9a031b609e279911ff820a5d18d1d7532bead651ede6beb2c"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 111000026081546
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285763, 'matching_hash': 'ce75c9757255dcb1'}}}