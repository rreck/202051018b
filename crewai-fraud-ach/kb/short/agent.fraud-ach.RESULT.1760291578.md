```json
{
  "id": "3567a489c598ed72",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291578,
  "host_pid": "9e6742732c60:1",
  "hash": "5774939c562f73cdc6a34a59cea8d2b7377ab78003b2c0f97f840d80780cf3d2",
  "cid": "QmV15774939c562f73cdc6a34a59cea8d2b7377ab780",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291578,
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
      "evaluated_at": 1760291578
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
  "sig": "3a89ed21769e91b793e57b1b5db8a7318d206ea49e5f13346a8c53cddfc251c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596811195
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 39256654, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285765, 'matching_hash': '0f37bc2cbfa5aec6'}}}