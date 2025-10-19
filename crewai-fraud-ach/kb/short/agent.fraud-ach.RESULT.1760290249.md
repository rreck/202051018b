```json
{
  "id": "0c6f3487c30ca894",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290249,
  "host_pid": "9e6742732c60:1",
  "hash": "11c47f5c699b67d0bd08b306d5067c22b75d27a8390cf46f850142240a243025",
  "cid": "QmV111c47f5c699b67d0bd08b306d5067c22b75d27a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290249,
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
      "evaluated_at": 1760290249
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
  "sig": "5316fdea78d7cb9c6e68ae1582bcc07c2fd9903eb15309b7b9fdae0e4471a5ff"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279221197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 64745400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285765, 'matching_hash': '706f719d80b46657'}}}