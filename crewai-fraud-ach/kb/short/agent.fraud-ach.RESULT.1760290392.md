```json
{
  "id": "3f3d131f55e82b6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290392,
  "host_pid": "9e6742732c60:1",
  "hash": "c979d6d80a1d8c47bb4dec02790ee6470a41716eebe5c96a40f60d544855d016",
  "cid": "QmV1c979d6d80a1d8c47bb4dec02790ee6470a41716e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290392,
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
      "evaluated_at": 1760290392
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
  "sig": "7ffa46bd7433be56a6dad7dc6465ea7f08f27c7243fb58274d262cc514d37ce1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028058978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 149, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 148, 'first_seen': 1760285764, 'matching_hash': '1bb3ef3babc34591'}}}een': 1760285763, 'matching_hash': '4e5cfda15432477b'}}}