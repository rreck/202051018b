```json
{
  "id": "8fc6cde54d4eba7d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288026,
  "host_pid": "9e6742732c60:1",
  "hash": "91f4619c595a928064258056ffb847f353cb4c666fb74a63c55f430887361f7a",
  "cid": "QmV191f4619c595a928064258056ffb847f353cb4c66",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288026,
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
      "evaluated_at": 1760288026
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
  "sig": "6bbe27f18c2cf70e1bbd599fde4484a148ff3cdba4f032e1250f37dbdbac068f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468256911
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 14521760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285765, 'matching_hash': 'b0ec3a54cf0504a9'}}}